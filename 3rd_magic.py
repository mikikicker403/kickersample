
#-*- coding:utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('program start')
#logging.disable(logging.CRITICAL)

deck=('A_C','A_D','A_H','A_S',
'2_C','2_D','2_H','2_S',
'3_C','3_D','3_H','3_S',
'4_C','4_D','4_H','4_S',
'5_C','5_D','5_H','5_S',
'6_C','6_D','6_H','6_S',
'7_C','7_D','7_H','7_S',
'8_C','8_D','8_H','8_S',
'9_C','9_D','9_H','9_S',
'10_C','10_D','10_H','10_S',
'J_C','J_D','J_H','J_S',
'Q_C','Q_D','Q_H','Q_S',
'K_C','K_D','K_H','K_S')

def AssistantOrdersCards():
    print('Cards are character strings as shown below')
    print('Ordering is:',deck)

if __name__=='__main__':
    AssistantOrdersCards()
    pass


    