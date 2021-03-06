#!/usr/bin/python2
# Copyright 2015 Open vStorage NV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from source.app import app
from source.tools.configuration import Configuration

if __name__ == '__main__':
    context = ('server.crt', 'server.key')
    config = Configuration()
    config.migrate()
    app.run(host='0.0.0.0',
            port=8500,
            ssl_context=context,
            threaded=True)
