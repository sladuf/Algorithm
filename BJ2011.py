# 21.03.02 [암호코드]
'''
-1 -2 번째 dp를 고려하는 규칙 문제
'''
import sys

n = ['0'] + list(sys.stdin.readline().strip())

#0으로 시작할 수 없음
if n[1] == '0':
	print(0)
else:
	dp = [0 for x in range(len(n))]
	#dp[0] = 1 : dp[2]에서 자기 자신을 더해주기 위함
	dp[0] = 1
	dp[1] = 1
	for i in range(2, len(n)):
		#0이고 앞에 1,2가 아니면 해석 불가능 하므로 종료
		if n[i] == 0 and n[i-1] > 2:
			print(0)
			sys.exit(0)
		#앞 자리가 만약 0이라면 혼자 해석 불가능 함
		if int(n[i]) >= 1:
			dp[i] = dp[i-1]
		#10~26 사이의 두 자리 수 만 알파벳으로 변환이 가능함
		#두 칸 앞 방법을 추가
		if 10<= int(n[i-1]+n[i]) <= 26:
			dp[i] += dp[i-2]

	print(dp[-1]%1000000)