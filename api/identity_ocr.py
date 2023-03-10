from requests import Response
from api.base_api import BaseApi


class IdentityOcr(BaseApi):

    def identity_ocr(self, image_path) -> Response:
        url = "https://[DOMAIN]/identity/ocr"
        if image_path:
            image = {'image': open(image_path, 'rb')}
            response = self.request('POST', url, headers=self.headers, files=image)
        else:
            response = self.request('POST', url, headers=self.headers)
        return response
