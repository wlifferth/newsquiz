import hashlib

class Headline:
    def __init__(self,
            text,
            datetime,
            publisher,
            link,
            author=None,
            summary=None,
            image_link=None,
            image_credit=None,
            **kwargs):
        self.text = text
        self.datetime = datetime
        self.publisher = publisher
        self.link = link
        self.author = author
        self.summary = summary
        self.image_link = image_link
        self.image_credit = image_credit
        self.uid = hashlib.md5((self.text+self.publisher).encode()).hexdigest()

    def __str__(self):
        s = 'HEADLINLE'
        for k, v in self.__dict__.items():
            s += '\n    {}:    {}'.format(k, v)
        s += '\n'
        return s

    @staticmethod
    def from_str(text):
        lines = text.split('\n')
        if lines[0] != 'HEADLINLE':
            raise Exception('Error parsing Headline from string. First line should be \'HEADLINE\', instead got \'{}\''.format(lines[0]))
        attributes = dict()
        for line in lines[1:]:
            k, v = line.strip().split(':    ')
            attributes[k] = v
        return Headline(**attributes)
            
