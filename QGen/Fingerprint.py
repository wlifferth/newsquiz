import numpy as np

class Fingerprint:
    def __init__(self, embedding=None, fingerprint_list=None):
        if embedding is not None:
            if len(embedding) != 50:
                raise Exception("Fingerprint  should be given an embedding that contains 50 integers. Was given {}".format(len(embedding)))
            self.value = np.array(embedding, dtype=int)
        elif fingerprint_list is not None:
            self.value = Fingerprint.mean(fingerprint_list)

    @staticmethod
    def mean(fingerprint_list):
        return np.mean(np.hstack([fp.value for fp in fingerprint_list]), axis=0)
