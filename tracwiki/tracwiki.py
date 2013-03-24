#!/usr/bin/env python

"""
Checkout and commit wiki pages stored on a trac server.


First use the config option to configure the server, after this, the checkout
and commit commands are available.
"""

import sys
import json
import argparse
import xmlrpclib

config_file = ".trac_config"

def docSplit(func):
    """
    Return the header of the docstring of a function.

    @arg func: A function.
    @type func: function
    """
    return func.__doc__.split("\n\n")[0]
#docSplit

def config(args):
    """
    Make a configuration file for a trac server.

    @arg args: Argparse argument list.
    @type args: object
    """
    protocol, location = args.URL.split("://")
    configFile = open(config_file, "w")

    configFile.write(json.dumps({
        "protocol": protocol,
        "location": location,
        "username": args.USER,
        "password": args.PASS,
    }))
#config

def connect():
    """
    Use the data from the config file to connect to a trac server.

    @returns: An XMLRPC server object.
    @rtype: object
    """
    conf = json.loads(open(config_file, "r").read())

    return xmlrpclib.ServerProxy("%s://%s:%s@%s/login/xmlrpc" % (
        conf["protocol"], conf["username"], conf["password"],
        conf["location"]))
#connect

def checkout(args):
    """
    Retrieve a trac wiki page in plain text format.

    @arg args: Argparse argument list.
    @type args: object
    """
    args.FILE.write(connect().wiki.getPage(args.FILE.name))
#checkout

def commit(args):
    """
    Commit a trac wiki file.

    @arg args: Argparse argument list.
    @type args: object
    """
    connect().wiki.putPage(args.FILE.name, args.FILE.read(), {})
#checkout

def main():
    """
    Main entry point.
    """
    default_parser = argparse.ArgumentParser(add_help=False)
    default_parser.add_argument("FILE", type=argparse.FileType("a+"),
        help="name of the page")

    usage = __doc__.split("\n\n\n")
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=usage[0], epilog=usage[1])
    subparsers = parser.add_subparsers()

    parser_config = subparsers.add_parser("config",
        description=docSplit(config))
    parser_config.add_argument("URL", type=str,
        help="base url of the trac intallation")
    parser_config.add_argument("USER", type=str, help="user name")
    parser_config.add_argument("PASS", type=str, help="password")
    parser_config.set_defaults(func=config)

    parser_checkout = subparsers.add_parser("checkout",
        parents=[default_parser], description=docSplit(checkout))
    parser_checkout.set_defaults(func=checkout)

    parser_commit = subparsers.add_parser("commit",
        parents=[default_parser], description=docSplit(commit))
    parser_commit.set_defaults(func=commit)

    args = parser.parse_args()

    try:
        args.func(args)
    except ValueError, error:
        parser.error(error)
#main

if __name__ == "__main__":
    main()
