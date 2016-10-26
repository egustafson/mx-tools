""" CLI for mx-tools
"""

import os
from datetime import datetime
from sys import stdin

import click


@click.command()
def mbox_fwd_trace():
    isonow = datetime.now().isoformat()
    tmpfn = "/tmp/mxtrace-{}".format(isonow)
    msg = stdin.read()
    f = open(tmpfn+'.msg', 'w')
    f.write(msg)
    f.close()
    ##
    f = open(tmpfn+'.env', 'w')
    for (k,v) in os.environ.items():
        f.write("{}={}\n".format(k,v))
    f.close()
    ##
    click.echo("trace - {} bytes read.".format(len(msg)))

