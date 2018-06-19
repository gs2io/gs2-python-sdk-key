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


class Key(object):

    def __init__(self, params=None):
        if params is None:
            self.__key_id = None
            self.__owner_id = None
            self.__name = None
            self.__create_at = None
        else:
            self.set_key_id(params['keyId'] if 'keyId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)

    def get_key_id(self):
        """
        暗号鍵GRNを取得
        :return: 暗号鍵GRN
        :rtype: unicode
        """
        return self.__key_id

    def set_key_id(self, key_id):
        """
        暗号鍵GRNを設定
        :param key_id: 暗号鍵GRN
        :type key_id: unicode
        """
        self.__key_id = key_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        暗号鍵名を取得
        :return: 暗号鍵名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        暗号鍵名を設定
        :param name: 暗号鍵名
        :type name: unicode
        """
        self.__name = name

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Key, self).__getitem__(key)

    def to_dict(self):
        return {
            "keyId": self.__key_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "createAt": self.__create_at,
        }
