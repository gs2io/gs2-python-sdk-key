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

from gs2_key_client.model import *


class DescribeKeyResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__items = list(
            map(
                lambda data:
                Key(data)
                ,
                response['items']
            )
        )
        
        self.__next_page_token = unicode(response['nextPageToken']) if 'nextPageToken' in response.keys() and response['nextPageToken'] is not None else None

    def get_items(self):
        """
        暗号鍵を取得
        :return: 暗号鍵
        :rtype: list[Key]
        """
        return self.__items

    def get_next_page_token(self):
        """
        次のページを読み込むためのトークンを取得
        :return: 次のページを読み込むためのトークン
        :rtype: unicode
        """
        return self.__next_page_token

    def to_dict(self):
        """
        辞書配列に変換
        :return: 辞書配列
        :rtype: dict
        """
        return { 
            'items': map(lambda item: item.to_dict(), self.__items),
        
            'nextPageToken': self.__next_page_token,
        
        }