# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from zope.interface import Interface


class ILoginService(Interface):

    def get_user(userid):
        """
        Return the user object that represents the given userid, or None if
        there is no user for that ID.
        """

    def find_userid(username):
        """
        Find the unique user identifier for the given username or None if there
        is no user with the given username.
        """

    def check_password(userid, password):
        """
        Returns a boolean representing whether the given password is valid for
        the given userid.
        """
