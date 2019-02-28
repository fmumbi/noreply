import pandas as pd




class Slide:
    def __init__(self, ids, orientation, tags):
        self.ids = ids
        self.orientation = orientation
        self.tags = tags


def score(slide1, slide2):

    intersect = len(slide1.tags.intersection(slide2.tags))
    diff1 = len(slide1.tags.difference(slide2.tags))
    diff2 = len(slide2.tags.difference(slide1.tags))

    return(min(intersect, diff1, diff2))


def out_str(slides):
    out = str(len(slides)) + "\n"
    tempScore = 0
    for i in (range(0, len(slides)-2)):
        tempScore += score(slides[i], slides[i + 1])

        out += " ".join(slides[i].ids)
        out += "\n"
    out += " ".join(slides[len(slides) - 1].ids)
    print(tempScore)
    return out