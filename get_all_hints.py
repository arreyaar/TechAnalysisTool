from indicator import calculate
from indicator import com_to_text
from datetime import date


def get_all_hints():
	hose_indi = calculate('hose')
	hnx_indi = calculate('hnx')
	upcom_indi = calculate('upcom')
	today = date.today().strftime("%d-%m-%Y")
	texts = [f''' *Update {today}*
	_HOSE_, Parabolic SAR
	- Company {com_to_text(hose_indi['psar_up'],'HOSE',"par")} stop going down and reverse
	- Company {com_to_text(hose_indi['psar_down'],'HOSE',"par")} stop going up and reverse
	''',
	f'''
	_HNX_, Parabolic SAR
	- Company {com_to_text(hnx_indi['psar_up'],'HNX',"par")} stop going down and reverse
	- Company {com_to_text(hnx_indi['psar_down'],'HNX',"par")} stop going up and reverse
	
	''',
	f'''
	_UPCOM_, Parabolic SAR
	- Company {com_to_text(upcom_indi['psar_up'],'UPCOM',"par")} stop going down and reverse
	- Company {com_to_text(upcom_indi['psar_down'],'UPCOM',"par")} stop going up and reverse
	
	''',
	
	
	f'''
	_HOSE_, RSI
	- Company {com_to_text(hose_indi['overbought'],'HOSE',"rsi")} is overbought
	- Company {com_to_text(hose_indi['oversold'],'HOSE',"rsi")} is oversold
	''',
	
	f'''
	_HNX_, RSI
	- Company {com_to_text(hnx_indi['overbought'],'HNX',"rsi")} is overbought
	- Company {com_to_text(hnx_indi['oversold'],'HNX',"rsi")} is oversold
	''',
	
	f'''
	_UPCOM_, RSI
	- Company {com_to_text(upcom_indi['overbought'],'UPCOM',"rsi")} is overbought
	- Company {com_to_text(upcom_indi['oversold'],'UPCOM',"rsi")} is oversold
	''',
	
	f'''
	_HOSE_, Bollinger Band
	- Company {com_to_text(hose_indi['bbh'], 'HOSE', 'bb') } have close price higher than bollinger high band
	- Company {com_to_text(hose_indi['bbl'], 'HOSE', 'bb') } have close price lower than bollinger low band
	''',
	f'''
	_HNX_, Bollinger Band
	- Company {com_to_text(hnx_indi['bbh'], 'HNX', 'bb') } have close price higher than bollinger high band
	- Company {com_to_text(hnx_indi['bbl'], 'HNX', 'bb') } have close price lower than bollinger low band
	''',
	f'''
	_UPCOM_, Bollinger Band
	- Company {com_to_text(upcom_indi['bbh'], 'UPCOM', 'bb') } have close price higher than bollinger high band
	- Company {com_to_text(upcom_indi['bbl'], 'UPCOM', 'bb') } have close price lower than bollinger low band
	''',
	
	f'''
	_HOSE_, SMA14
	- Company {com_to_text(hose_indi['sma_up'], 'HOSE', 'sma-14') } cut and have close price higher than sma 14 days
	- Company {com_to_text(hose_indi['sma_down'], 'HOSE', 'sma-14') } cut and have close price lower than sma 14 days
	''',
	f'''
	_HNX_, SMA14
	- Company {com_to_text(hnx_indi['sma_up'], 'HNX', 'sma-14') } cut and have close price higher than sma 14 days
	- Company {com_to_text(hnx_indi['sma_down'], 'HNX', 'sma-14') } cut and have close price lower than sma 14 days
	''',
	f'''
	_UPCOM_, SMA14
	- Company {com_to_text(upcom_indi['sma_up'], 'UPCOM', 'sma-14') } cut and have close price higher than sma 14 days
	- Company {com_to_text(upcom_indi['sma_down'], 'UPCOM', 'sma-14') } cut and have close price lower than sma 14 days
	'''
	]
	str = ""    
	return str.join(texts)