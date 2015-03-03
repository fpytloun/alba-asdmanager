#!/usr/bin/python2
# Copyright 2015 CloudFounders NV
# All rights reserved


from source.app import app
from source.tools.configuration import Configuration

if __name__ == '__main__':
    context = ('server.crt', 'server.key')
    config = Configuration()
    app.run(host='0.0.0.0',
            port=int(config.data['ports']['service']),
            debug=True,
            ssl_context=context)