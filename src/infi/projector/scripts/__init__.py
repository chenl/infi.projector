from sys import argv

#pylint: disable=R0801

def projector(argv=argv[1:]):
    from os import environ
    from logging import basicConfig, INFO, DEBUG
    from sys import stderr
    from infi.projector.commandline_parser import parse_commandline_arguments
    basicConfig(level=DEBUG if environ.get("DEBUG") else INFO, stream=stderr)
    parse_commandline_arguments(argv)