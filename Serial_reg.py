def Uart_init():
                         
                          #0x7E201000      Uart main address
                          #0x30             CR register address
                          #0x2C             Line control register
                         uart_CR = 0x7E201030
                         uart_LCRH = 0x7E20102C
                         
                         def setBit_en(n, k):
                                                  return (n | ( ~(1 << (k - 1))))
                         # Driver code
                         n = uart_CR
                         k = 1
                         print(setBit_en(n, k))
                         
                         def setBit_WL(n, k):
                                                  return (n | ( ~(3 << (k - 1))))
                         # Driver code
                         n = uart_LCRH
                         k = 5
                         print(setBit_WL(n, k))
Uart_init()
                         