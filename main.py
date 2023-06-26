import random
import pandas as pd
from loguru import logger


from utils import Minter, Bridger
from info import keys
from config import shuffle, MODE, chain, to_chain, moralis_api, delay, count
from config import minter_mode, bridger_mode

def main():
    wallets, results = [], []
    print(f'\n{" " * 32}автор - https://t.me/iliocka{" " * 32}\n')
    if shuffle:
        random.shuffle(keys)

    for key in keys:
        if MODE == 'minter':
            logger.info('Запущен минтер HFWC1...')
            mint_ = Minter(key, chain, count, delay, minter_mode)
            res = mint_.mint()
            wallets.append(res[0]), results.append(res[1])
        if MODE == 'bridger':
            logger.info('Запущен бриджер HFWC1...')
            bridge_ = Bridger(key, chain, to_chain, delay, moralis_api, bridger_mode)
            res = bridge_.bridge()
            wallets.append(res[0]), results.append(res[1])

    if MODE == 'minter':
        logger.success('mинетинг закончен...')
    else:
        logger.success('бриджетинг закончен...')
    res = {'address': wallets, 'result': results}
    df = pd.DataFrame(res)
    df.to_csv('results.csv', mode='a', index=False)

    print(f'\n{" " * 32}автор - https://t.me/iliocka{" " * 32}\n')
    print(f'\n{" " * 32}donate - EVM 0xFD6594D11b13C6b1756E328cc13aC26742dBa868{" " * 32}\n')
    print(f'\n{" " * 32}donate - trc20 TMmL915TX2CAPkh9SgF31U4Trr32NStRBp{" " * 32}\n')

if __name__ == '__main__':
    main()


