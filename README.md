# LineBOT_Framework

1.Copy "LineBOT_Framework" and change the name for your project<br>
  1.1 install anaconda and update all packages <br>
  1.2 create new python(version>=3.7) enveronment such as "LineBOT" (using conda : conda create -n LineBOT python=3.7 anaconda)<br>
  1.3 install these packages using command below <br>
    1.3.1 conda install -c conda-forge requests<br>
    1.3.2 conda install -c conda-forge flask<br>
    1.3.3 pip install line-bot-sdk<br>
    1.3.4 pip install ngrok-api<br>

2.Open project using vscode [under enveronement ("LineBOT")]<br>
  2.1 Open custom/Config.py<br>
  2.2 Change values of CHANNEL_SECRET,CHANNEL_ACCESS_TOKEN,NGROK_TOKEN_API using values from LineOA and Ngrok<br>

3.Create and config Line Dev via https://developers.line.biz/en/<br>
  2.1 Create new chanel in Agent<br>
  2.2 Setting profile icon  <br>
  2.3 Copy "channel secret" value and past for CHANNEL_SECRET in custom/Config.py<br>
  2.4 Create and copy "channel access token" for CHANNEL_ACCESS_TOKEN in custom/Config.py<br>
  2.5 Set "Auto-reply messages" to "Disable"<br>

4.Register & Using ngrok<br>
  4.1 Config ngrok following get start page (https://dashboard.ngrok.com/get-started/setup,using port 5000 for this example project)<br>
  4.2 Create api token via https://dashboard.ngrok.com/api<br>
  4.3 Copy api token and past for NGROK_TOKEN_API in custom/Config.py<br>

5.Setting Line webhook<br>
  5.1 Run 1_run_ngrok.bat<br>
  5.2 Copy forwarding and past to Webhook URL in LineDev (https://developers.line.biz/en/)<br>
  5.3 enable for Use webhook,Webhook redelivery,Error statistics aggregation<br>
6.Start to implement the code at custom/WebhookManager.py<br>
