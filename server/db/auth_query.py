# Copyright 2017 Intel Corporation
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
# ------------------------------------------------------------------------------

import rethinkdb as r

from api.errors import ApiNotFound


async def create_auth_entry(conn, auth_entry):
    return await r.table('auth').insert(auth_entry).run(conn)


async def fetch_info_by_user_id(conn, user_id):
    auth_info = await r.table('auth').get(user_id).run(conn)
    if auth_info is None:
        raise ApiNotFound(
            "Not Found: "
            "No user with id '{}' exists.".format(user_id)
        )
    return auth_info
