import random

def reply(text):

    # 명령어 종류를 확인하려면?
    thanks_letter = '더울 때, 배고플 때, 시끄러울 때, 졸릴 때, 피곤할 때, 즐거울 때, 홍루이젠 먹을 때, 엠티 때, 술 취했을 때, 그리고 공부할 때 모든 시간 함께 해주셔서 영광이었습니다. - Jin Kim', '감사인사2', '감사인사3\n감사합니다!'

    if "감사편지" in text:
        letter = str(random.choice(thanks_letter))
        return letter
    else:
        return None
