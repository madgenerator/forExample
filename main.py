#for with list
testList = [1,2,3,4]
for number in testList:
  print(number)

#for simple use
for i in range(10):
  print("안녕하세요",i+1,"번째 인사")

#for : index and object
rainbow=["빨","주","노","초","파","남","보","검"]
for i in range(len(rainbow)):
  print("무지개의",i+1,"번째 색깔은",rainbow[i],"입니다")

#month
days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(len(days)):
  print(i+1,"월의 날짜수는",days[i],"일 입니다.")

#favorite member
members=["토마스", "막스","정훈","블라드","유토"]
for i in range(len(members)):
  print("내가",i+1,"번째로 좋아하는 멤버는",members[i],"입니다")

