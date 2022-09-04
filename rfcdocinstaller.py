import os
import wget
import time

class Task(object):
    def getData(self, page):
        url1 = "http://www.rfc-editor.org/pdfrfc/rfc"
        url2 = "http://www.rfc-editor.org/rfc/rfc"
        for i in range(1, page):
            urlpdf1 = url1 + str(i) + ".txt.pdf"
            urlpdf2 = url2 + str(i) + ".pdf"
            print("\n")
            print("page ", str(i))
            print("\n")

            if os.path.exists("rfc" + str(i) + ".txt.pdf"):
                continue

            try:
                begin = time.perf_counter()
                wget.download(urlpdf1)
                end = time.perf_counter()
                print("\n")
                print(f"{ end - begin:0.4f} seconds")
            except:
                print("\n")
                print("try ", str(i))
                try:
                    
                    if os.path.exists("rfc" + str(i) + ".pdf"):
                        continue
                    
                    begin = time.perf_counter()
                    wget.download(urlpdf2)
                    end = time.perf_counter()
                    print("\n")
                    print(f"{ end - begin:0.4f} seconds")
                except:
                    print("\n")
                    print("none ", str(i))

    def run(self):
        self.getData(9145)

if __name__ == '__main__':
    print("Enter Download Path : ")
    downloadPath = input()
    if os.path.isdir(downloadPath):
        print("Please Download Folder :")
        downloadFolder = input()
        os.chdir(downloadPath)
        if not (os.path.exists(downloadFolder)):
            os.mkdir(downloadFolder)

        if os.system != "Windows":
            os.chdir(downloadPath + "\\" + downloadFolder)
        else:
            os.chdir(downloadPath + "/" + downloadFolder)

        task = Task()
        task.run()
    else:
        print("\nEdit path")