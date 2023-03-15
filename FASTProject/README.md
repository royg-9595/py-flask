Step 1:
Implement https://testdriven.io/blog/fastapi-docker-traefik/ in your github library with a README file for step by step execution. Your code should run and the apis should work.

1.	In VS code opened a blank folder named XQuantum (created in File explorer), later executed the command python3.11 -m venv venv.
2.	Then I used venv\Scripts\activate.batto activate virtual environment. The command given in blog is different from which I used. My system runs on Windows, while blog is written for MAC/Linux.
3.	Created the files and folders as instructed in blog, using VS code.
├── app
│   ├── __init__.py
│   └── main.py
└── requirements.txt
4.	Added 
fastapi==0.89.1
uvicorn==0.20.0 to requirements.txt file.
5.	Then executed the command pip install -r requirements.txt in VS code Powershell.
6.	FastAPI and starlette is installed. Uvicorn is already exists in my PC.
7.	After running the simple FastAPI sample program, A website began in port 127.0.0.1:8000 showing output {"hello":"world"}.
8.	Killed the server by clicking Cntrl+C. And erased the app environment.

Docker
1.	Created a txt named Dockerfile in the directory.
2.	Then pasted the file shown in blog.
3.	I don’t have docker in my system, I have installed docker. Updated wsl using command wsl –update.
4.	Then I copied the link shown in my docker and run it in my project terminal and started building the slim image. Command - docker-compose build
5.	Now again run the command shown in the blog, docker-compose up -d in my project terminal.
6.	Routed to the localhost link shown, My app server is running out there. I can see the same previous output. (hello world).
7.	Gone through the command, to check if there any errors, docker-compose logs -f.
