##      1       ##
# def phone_format(n):   
#         if n.isnumeric() :
#             if len(n) >10 or len(n) <10:
#                 print('Digits must be in length of 10, not more or less"')
#             elif (int(n)) < 0:
#                 print('Input only positive number')
#             else:  
#                 x = ''
#                 y = ''
#                 z = ''
#                 for i in n:
#                     if n.index(i) <= 2:
#                         x += i
#                     elif 3<= n.index(i) <= 5:
#                         y += i
#                     elif 6<= n.index(i) <= 9:
#                         z += i
#                 return f'({x})-{y}-{z}'
#         elif n.isalnum():
#             print('Invalid input. No alphabet. ')
#         elif n.isascii():
#             print('Invalid input. No symbols.') 

# masukkan = input('Masukkan nomor = ')
# print(phone_format(masukkan))

##      2       ##
# list = [False,0,0,1,0,2]
# def move_zeros(n):
#     filtered_list = [x for x in n if isinstance(x, int) and x or isinstance(x, bool)]+[0]*(n.count(0)-1) 
#     return filtered_list

# print(move_zeros(list))

##      3       ##
# class Statistic:
#     def __init__(self,sample):
#         self.sample = sample
#     def mean(self, sample):
#         return sum(self.sample) / len(self.sample)

#     def mode(self, sample):
#         d= {}
#         for i in self.sample:
#             d.setdefault(i, 0)
#             d[i] += 1
#         # mx = max(d,key=d.get)
#         mx = max(d.values())
#         highest= []
#         for i, freq in d.items() :
#             if freq == mx:
#                 highest.append(i)
#         strings = [str(integer) for integer in highest]
#         a_string=''.join(strings)
#         return (int(a_string))
#         # return d[mx] if d[mx] > 1 else self.sample 
#     def median(self,sample):
#         self.sample.sort()
#         if len(self.sample) % 2 == 0:
#             md1 = self.sample[len(self.sample) // 2]
#             md2 = self.sample[len(self.sample) // 2 - 1]
#             return md1 + md2 / 2
#         else:
#             return self.sample[len(self.sample) // 2]
#     def variance(self, sample):
#         return self.mean([(i-self.mean) ** 2 for i in sample])
#     def stdev(self,sample):
#         return  self.variance(sample) ** (1/2)

# st = Statistic([1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,9,9,9,9,])
# print(st.mode([]))
# print(st.mean([]))
# print(st.median([]))
# print(st.stdev([]))


     