from functools import partial

from topik.singleton_registry import BaseRegistry, _base_register_decorator


class VectorizerRegistry(BaseRegistry):
    pass


# fill in the registration function
register = partial(_base_register_decorator, VectorizerRegistry)


# a nicer, more pythonic handle to our singleton instance
registered_vectorizers = VectorizerRegistry()


def vectorize(corpus, method="tfidf", **kwargs):
    """Represent documents as vectors in word-space.

    Note: bag-of-words model is implicitly used when no additional
    vectorization is called.
    """
    return VectorizerRegistry()[method](corpus, **kwargs)
