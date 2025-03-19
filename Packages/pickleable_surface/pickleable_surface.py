import pygame as pg

pgSurf = pg.surface.Surface

class PickleableSurface(pgSurf):
    def __init__(self, logger, *arg,**kwarg):
        size = arg[0]
        self.logger = logger

        # size given is not an iterable,  but the object of pgSurf itself
        if (isinstance(size, pgSurf)):
            pgSurf.__init__(self, size=size.get_size(), flags=size.get_flags())
            self.surface = self
            self.name='test'
            self.blit(size, (0, 0))

        else:
            pgSurf.__init__(self, *arg, **kwarg)
            self.surface = self
            self.name = 'test'

    def __getstate__(self):
        state = self.__dict__.copy()
        try:
            self.logger.info(f"Pickleing {self.__class__.__name__, self.__class__.__dict__}")
        except Exception as e:
            try:
                self.logger.error(f"Error pickling {self.__class__.__name__}: {e}")
            except Exception as logger_e:
                print(f"Pickleing {self.__class__.__name__, self.__class__.__dict__}")
                print(f"Error pickling {self.__class__.__name__}: {e},\n{logger_e}")

        try:
            surface = state["surface"]

            _1 = pg.image.tobytes(surface.copy(), "RGBA")
            _2 = surface.get_size()
            _3 = surface.get_flags()
            state["surface_string"] = (_1, _2, _3)
        except Exception as e:
            try:
                self.logger.error(f"Error unpickling {self.__class__.__name__}: {e}")
            except Exception as logger_e:
                print(f"Error unpickling {self.__class__.__name__}: {e},\n{logger_e}")
        return state

    def __setstate__(self, state):
        surface_string, size, flags = state["surface_string"]

        pgSurf.__init__(self, size=size, flags=flags)

        s=pg.image.frombytes(surface_string, size, "RGBA")
        state["surface"] =s
        self.blit(s,(0,0))
        self.surface=self
        self.__dict__.update(state)
