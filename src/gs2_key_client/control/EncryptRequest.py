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


class EncryptRequest(Gs2BasicRequest):

    class Constant(Gs2Key):
        FUNCTION = "Encrypt"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(EncryptRequest, self).__init__(params)
        if params is None:
            self.__key_name = None
        else:
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)
        if params is None:
            self.__data = None
        else:
            self.set_data(params['data'] if 'data' in params.keys() else None)

    def get_key_name(self):
        """
        暗号鍵の名前を指定します。を取得
        :return: 暗号鍵の名前を指定します。
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        暗号鍵の名前を指定します。を設定
        :param key_name: 暗号鍵の名前を指定します。
        :type key_name: unicode
        """
        if key_name is not None and not (isinstance(key_name, str) or isinstance(key_name, unicode)):
            raise TypeError(type(key_name))
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        暗号鍵の名前を指定します。を設定
        :param key_name: 暗号鍵の名前を指定します。
        :type key_name: unicode
        :return: this
        :rtype: EncryptRequest
        """
        self.set_key_name(key_name)
        return self

    def get_data(self):
        """
        暗号化するデータを取得
        :return: 暗号化するデータ
        :rtype: unicode
        """
        return self.__data

    def set_data(self, data):
        """
        暗号化するデータを設定
        :param data: 暗号化するデータ
        :type data: unicode
        """
        if data is not None and not (isinstance(data, str) or isinstance(data, unicode)):
            raise TypeError(type(data))
        self.__data = data

    def with_data(self, data):
        """
        暗号化するデータを設定
        :param data: 暗号化するデータ
        :type data: unicode
        :return: this
        :rtype: EncryptRequest
        """
        self.set_data(data)
        return self
