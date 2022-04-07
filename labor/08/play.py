import os
import matplotlib.pyplot as plt


class Play:
    def __init__(self, author: str, title: str, directory: str) -> None:
        self.author = author
        self.title = title
        self.actors = set()
        self.scenes = []
        self.__fetch_scenes(directory)

    def __fetch_scenes(self, directory: str) -> None:
        for filename in os.listdir(directory):
            if os.path.splitext(filename)[-1] == '.txt':
                self.scenes.append(Scene(directory+'/'+filename))
                self.actors.update(self.scenes[-1].actors)

    def scene_count(self, actor: str) -> int:
        return sum([1 for scene in self.scenes if actor.upper() in scene.actors])

    def show_charts(self) -> None:
        fig, (ax1, ax2) = plt.subplots(2, constrained_layout=True)
        fig.suptitle(f'{self.author}: {self.title}\nAppearances in scenes')
        actors = list(self.actors)
        scenes = [self.scene_count(a) for a in actors]
        ax1.barh(actors, scenes)
        ax1.set_xticks(range(1+max(scenes)))
        apps = [sum([s.speech_count(a) for s in self.scenes]) for a in actors]
        ax2.pie(apps, labels=actors)
        plt.show()


class Scene:
    def __init__(self, filename: str) -> None:
        self.actors = set()
        self.lines = None
        try:
            with open(filename) as file:
                self.lines = [line.strip() for line in file.readlines()]
                self.__fetch_actors()
        except FileNotFoundError:
            print(f'File {filename} is not available.')

    def __fetch_actors(self):
        for line in self.lines:
            if line != '' and line.upper() == line:
                self.actors.add(line)

    def speech_count(self, actor: str) -> int:
        return sum([1 for line in self.lines if line == actor.upper()])


# Példakód az osztályok és metódusaik használatára
if __name__ == '__main__':
    play = Play('Shakespeare', 'Hamlet (Act 1)', './hamlet-demo')
    print('Horatio appears in', play.scene_count('Horatio'), 'scenes')  # 2
    print('Hamlet appears in', play.scene_count('Hamlet'), 'scenes')  # 1
    print('Arthur appears in', play.scene_count('Arthur'), 'scenes')  # 0

    scene1 = Scene('hamlet-demo/act-1-scene-1.txt')
    hamlet1 = scene1.speech_count('Hamlet')
    print('Hamlet speaks', hamlet1, 'times in Scene 1')  # 0

    scene2 = Scene('hamlet-demo/act-1-scene-2.txt')
    hamlet2 = scene2.speech_count('Hamlet')
    print('Hamlet speaks', hamlet2, 'times in Scene 2')  # 33

    cameo = scene2.speech_count('Shakespeare')
    print('Shakespeare speaks', cameo, 'times in Scene 2')  # 0

    missing = Scene('hamlet-demo/act-666-scene-45.txt')  # error message

    play.show_charts()

    play = Play('William Shakespeare', 'Hamlet', './hamlet-full')
    play.show_charts()
