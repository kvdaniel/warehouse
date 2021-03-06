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

import babel.dates
import pretend

from warehouse.i18n import filters


def test_format_date(monkeypatch):
    formatted = pretend.stub()
    format_date = pretend.call_recorder(lambda *a, **kw: formatted)
    monkeypatch.setattr(babel.dates, "format_date", format_date)

    request = pretend.stub(locale=pretend.stub())
    ctx = pretend.stub(get=pretend.call_recorder(lambda k: request))

    args = [pretend.stub(), pretend.stub()]
    kwargs = {"foo": pretend.stub()}

    assert filters.format_date(ctx, *args, **kwargs) is formatted

    kwargs.update({"locale": request.locale})
    assert format_date.calls == [pretend.call(*args, **kwargs)]
