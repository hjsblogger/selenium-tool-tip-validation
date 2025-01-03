# Tool-Tip text validation with Selenium & Python

<img width="700" height="400" alt="Automation" src="https://github.com/user-attachments/assets/c438af79-e9e3-441a-9eec-92b59f22dc9c">

Repo Inspiration : [YouTube Video](https://www.youtube.com/watch?v=qItS8AXOwww)

## Pre-requisites for test execution

**Step 1**

Create a virtual environment by triggering the *virtualenv venv* command on the terminal

```bash
virtualenv venv
```
<img width="1418" alt="VirtualEnvironment" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/89beb6af-549f-42ac-a063-e5f715018ef8">

**Step 2**

Navigate the newly created virtual environment by triggering the *source venv/bin/activate* command on the terminal

```bash
source venv/bin/activate
```

**Step 3**

Procure the LambdaTest User Name and Access Key by navigating to [LambdaTest Account Page](https://accounts.lambdatest.com/security). You might need to create an an account on LambdaTest since it is used for running tests on the cloud Grid.

<img width="1288" alt="LambdaTestAccount" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/9b40c9cb-93a1-4239-9fe5-99f33766a23a">

**Step 4**

Add the LambdaTest User Name and Access Key in the *Makefile* that is located in the parent directory. Once done, save the Makefile.

![Makefile](https://github.com/user-attachments/assets/9789bc91-b2e3-4a38-b31b-03f9c6a792c6)

## Dependency/Package Installation

Run the *make install* command on the terminal to install the desired packages (or dependencies) - Pytest, Selenium, etc.

```bash
make install
```
<img width="1404" alt="Make-Install" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/4cb16443-4411-4f11-8692-aa7290cded0b">

<img width="1404" alt="Make-Install-2" src="https://github.com/hjsblogger/web-scraping-with-python/assets/1688653/8c7e8938-5584-480b-ad04-002b53827396">

With this, all the dependencies and environment variables are set. Instead of PyUnit/*unittest*, the Pytest framework is used for test execution. The
[LambdaTest Selenium Playground - Input Form Demo](https://www.lambdatest.com/selenium-playground/input-form-demo) website is used for demonstration purposes.

Follow the below mentioned steps to run automated tests using Selenium Python:

**Step 1**

Change the *EXEC_PLATFORM* variable to *local* in [.env](https://github.com/hjsblogger/selenium-tool-tip-validation/blob/master/.env) in case you want to run tests on your local machine.

Alternatively, you can also set *EXEC_PLATFORM* environment variable to *cloud*. Trigger the command *export EXEC_PLATFORM=local* on the terminal.


**Step 2**

Trigger the command *make clean* to clean the remove _pycache_ folder(s) and .pyc files

<img width="512" src="https://github.com/user-attachments/assets/62d0a440-3cdb-4721-95a2-f4d3492f2a47">

**Step 3**

Trigger the respective *make* command on the terminal to run the test(s). For example, run the command *make tool_tip_verification_demo* for triggering the test that validates the tool-tip.

<img width="1417" alt="MakeCommand" src="https://github.com/user-attachments/assets/603cc2c9-f0d0-4d9b-a70c-c4d85c4c5072" />

As seen above, the test execution was successful and the status is "Completed". You can find the status of test execution in the [LambdaTest Automation Dashboard](https://automation.lambdatest.com/build).

<img width="1439" alt="Dashboard_1" src="https://github.com/user-attachments/assets/5445d389-93dc-4a27-9f65-baa1de8d3902" />

<img width="1439" alt="Dashboard_2" src="https://github.com/user-attachments/assets/cff0583e-9acf-4860-befc-0de447083c5a" />

## Have feedback or need assistance?
Feel free to fork the repo and contribute to make it better! Email to [himanshu[dot]sheth[at]gmail[dot]com](mailto:himanshu.sheth@gmail.com) for any queries or ping me on the following social media sites:

<b>LinkedIn</b>: [@hjsblogger](https://linkedin.com/in/hjsblogger)<br/>
<b>Twitter</b>: [@hjsblogger](https://www.twitter.com/hjsblogger)
