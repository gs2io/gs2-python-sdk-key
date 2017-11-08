# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_key_client.Gs2Key import Gs2Key


class CreateKeyRequest(Gs2BasicRequest):

    class Constant(Gs2Key):
        FUNCTION = "CreateKey"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateKeyRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)

    def get_name(self):
        """
        暗号鍵の名前を取得
        :return: 暗号鍵の名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        暗号鍵の名前を設定
        :param name: 暗号鍵の名前
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        暗号鍵の名前を設定
        :param name: 暗号鍵の名前
        :type name: unicode
        :return: this
        :rtype: CreateKeyRequest
        """
        self.set_name(name)
        return self
