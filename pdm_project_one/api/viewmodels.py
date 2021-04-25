from typing import Optional

from starlette.requests import Request


class ViewModelBase:

    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__


class DesignViewModel(ViewModelBase):

    def __init__(self, request: Request) -> object:
        super().__init__(request)

        self.email = ''
        self.final_text = ''
        self.final_image = None

    async def load(self):
        form = await self.request.form()
        # self.email = form.get('email').lower().strip()
        self.final_text = form.get('wbtext').upper().strip()
        self.final_image = form.get('upload-file')
        return {'text': self.final_text, 'image': self.final_image}
