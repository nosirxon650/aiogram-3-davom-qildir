from aiogram import Router, types, F
from keyboards.inline.cats import cats
router = Router()


@router.message(F.text == "salom")
async def SalomBot(message: types.Message):
    await message.answer_photo(photo="https://storage.googleapis.com/pod_public/1300/151089.jpg", caption="Mushiklar dokoniga xush kelibsiz", reply_markup=cats)
    
    
@router.callback_query(F.data == "uy")
async def Uy(call: types.CallbackQuery):
    await call.message.answer("Bunday mushuklar qolmadi")