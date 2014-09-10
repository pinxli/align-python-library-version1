from HttpClient.Curl import Curl

def main():
	cl = Curl()
	cl.get('http://localhost:8000/')

if __name__ == "__main__":
    main()