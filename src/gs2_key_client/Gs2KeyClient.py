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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2KeyClient(AbstractGs2Client):

    ENDPOINT = "key"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2KeyClient, self).__init__(credential, region)

    def create_key(self, request):
        """
        暗号鍵を新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_key_client.control.CreateKeyRequest.CreateKeyRequest
        :return: 結果
        :rtype: gs2_key_client.control.CreateKeyResult.CreateKeyResult
        """
        body = { 
            "name": request.get_name(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.CreateKeyRequest import CreateKeyRequest
        from gs2_key_client.control.CreateKeyResult import CreateKeyResult
        return CreateKeyResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key",
            service=self.ENDPOINT,
            component=CreateKeyRequest.Constant.MODULE,
            target_function=CreateKeyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def decrypt(self, request):
        """
        復号化処理を実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_key_client.control.DecryptRequest.DecryptRequest
        :return: 結果
        :rtype: gs2_key_client.control.DecryptResult.DecryptResult
        """
        body = { 
            "data": request.get_data(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.DecryptRequest import DecryptRequest
        from gs2_key_client.control.DecryptResult import DecryptResult
        return DecryptResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key/" + str(("null" if request.get_key_name() is None or request.get_key_name() == "" else url_encoder.encode(request.get_key_name()))) + "/decrypt",
            service=self.ENDPOINT,
            component=DecryptRequest.Constant.MODULE,
            target_function=DecryptRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_key(self, request):
        """
        暗号鍵を削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_key_client.control.DeleteKeyRequest.DeleteKeyRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.DeleteKeyRequest import DeleteKeyRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key/" + str(("null" if request.get_key_name() is None or request.get_key_name() == "" else url_encoder.encode(request.get_key_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteKeyRequest.Constant.MODULE,
            target_function=DeleteKeyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_key(self, request):
        """
        暗号鍵の一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_key_client.control.DescribeKeyRequest.DescribeKeyRequest
        :return: 結果
        :rtype: gs2_key_client.control.DescribeKeyResult.DescribeKeyResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.DescribeKeyRequest import DescribeKeyRequest

        from gs2_key_client.control.DescribeKeyResult import DescribeKeyResult
        return DescribeKeyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key",
            service=self.ENDPOINT,
            component=DescribeKeyRequest.Constant.MODULE,
            target_function=DescribeKeyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def encrypt(self, request):
        """
        暗号化処理を実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_key_client.control.EncryptRequest.EncryptRequest
        :return: 結果
        :rtype: gs2_key_client.control.EncryptResult.EncryptResult
        """
        body = { 
            "data": request.get_data(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.EncryptRequest import EncryptRequest
        from gs2_key_client.control.EncryptResult import EncryptResult
        return EncryptResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key/" + str(("null" if request.get_key_name() is None or request.get_key_name() == "" else url_encoder.encode(request.get_key_name()))) + "/encrypt",
            service=self.ENDPOINT,
            component=EncryptRequest.Constant.MODULE,
            target_function=EncryptRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def get_key(self, request):
        """
        暗号鍵を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_key_client.control.GetKeyRequest.GetKeyRequest
        :return: 結果
        :rtype: gs2_key_client.control.GetKeyResult.GetKeyResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_key_client.control.GetKeyRequest import GetKeyRequest

        from gs2_key_client.control.GetKeyResult import GetKeyResult
        return GetKeyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/key/" + str(("null" if request.get_key_name() is None or request.get_key_name() == "" else url_encoder.encode(request.get_key_name()))) + "",
            service=self.ENDPOINT,
            component=GetKeyRequest.Constant.MODULE,
            target_function=GetKeyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
