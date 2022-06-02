# AVA-Crypto
<p>AVA Crypto is a dashboard that allows you to have a global view of your crypto wallet.</p>
<p>Thanks to Covalent and Coingecko API, we give you the possibility to have all balance, history, and transactions of your crypto wallets. You can also have the global balance of all your wallets. Lastly, AVA Crypto offers you the current price in a selection of cryptocurrencies.</p>
<p>To visualize all these features, we have developed a Dash application , which is deployable locally, or globally using Heroku.</p>
<p>Finally, we have linked a database to our app, in this way your informations remains when you log into your account.</p>

## Locally deployable (with Dash)
<p>Install <code>requirements.txt</code> to have all the necessary libraries to launch our app</p>
<pre><code>pip install -r requirements.txt</code></pre>
<p>Now launch the <code>main.py</code> file to run the dash application locally on your web browser</p>

## Globally deployable (with Heroku)
<p>Login into Heroku</p>
<pre><code>heroku login</code></pre>
<p>Clone the repository github heroku</p>
<pre><code>heroku git:clone -a avacrypto</code>
<code>cd avacrypto</code></pre>
<p>After that, you have to build the project and restart it</p>
<pre><code>heroku plugins:install heroku-builds</code>
<code>heroku builds:cancel</code>
<code>heroku restart</code></pre>
<p>To finish, deploy the application in Heroku</p>
<pre><code>git add .</code>
<code>git commit -am "YOUR COMMIT"</code>
<code>git push --force heroku main</code></pre>
