import math 

class ScanBooks: 

    def __init__(self, books, libraries, days): 
        self.libraries = libraries
        self.books = books
        self.days = days


    def calculateScore(self, indexes, booksperday, velocity): 
        sumOfBooks = 0
        for i in indexes:
            sumOfBooks += self.books[i]
        return sumOfBooks/(math.ceil(len(indexes) / booksperday) + velocity)

    def gradeLibraries(self): 
        result = {}
        i = 0 
        for lib  in self.libraries:
            result[i] = self.calculateScore(lib[1], lib[0][2], lib[0][1])
            i += 1
        return sorted(result, key=result.get, reverse=True)

    def getSchedule(self): 
        schedule = {}
        rates = self.gradeLibraries()
        for a in rates: 
            schedule[a] = sum(schedule.values()) + self.libraries[a][0][1] 
        return schedule       

    def scanFacility(self, libraryBooks, books): 
        index = None
        bookScore = 0 
        for b in libraryBooks: 
            if b not in books: 
                pass
            else:
                # print('this is b {}'.format(b))
                for c in books: 
                    if books[b] > bookScore: 
                        bookScore = books[b] 
                        index = b 
        return index

    def run(self): 
        rates = self.gradeLibraries()
        # libraries = self.libraries
        scanned = {}
        schedule = self.getSchedule()
        books = {i : self.books[i] for i in range(0, len(self.books))}
       
        for j in schedule: 
            scanned[j] = [[j, 0], []]

        for i in range(self.days): 
            if books: 
                print('Day {}'.format(i)) 
                for j in rates: 
                    if j in schedule: 
                        if schedule[j] <= i: 
                            toScann = 0
                            while toScann < libraries[j][0][2]: # update to use L[N]
                                if len(books) == 0 or len(self.libraries[j][1]) == 0:  
                                    pass
                                else:
                                    print('Scanning from facility {}'.format(j))
                                    scannedBooks = self.scanFacility(self.libraries[j][1], books)
                                    print(self.libraries[j][1])
                                    if scannedBooks is not None: 
                                        books.pop(scannedBooks) 
                                        self.libraries[j][1].remove(scannedBooks)
                                        scanned[j][1].append(scannedBooks)
                                        scanned[j][0][1] = len(scanned[j][1])
                                    else: 
                                        pass
                                toScann += 1 
                    else: 
                        pass
            else: 
                pass 

        print('Scanning process complete') 
        print(scanned)            
        # return scanned

books = [1, 2, 3, 6, 5, 4]
libraries = [
    [
        [5, 2, 2], 
        [0, 1, 2, 3, 4]
    ], 
    [
        [4, 3, 1], 
        [0, 2, 3, 5]
    ]
]   

days = 7 
ScanBooks(books, libraries, days).run()