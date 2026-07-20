const typingEl = document.getElementById('typing');

async function sendMessage(text){
  appendMessage('You', text, 'user');
  showTyping(true);
  try{
    const res = await fetch('/api/message', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: text})
    });
    const data = await res.json();
    showTyping(false);
    appendMessage('Bot', data.reply, 'bot');
  }catch(e){
    showTyping(false);
    appendMessage('Bot', 'Network error. Please try again.', 'bot');
  }
}

function appendMessage(who, text, cls){
  const chat = document.getElementById('chat');
  const div = document.createElement('div');
  div.className = 'message ' + cls;
  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.innerHTML = `<strong>${who}:</strong> ${escapeHtml(text)}`;
  div.appendChild(bubble);
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function escapeHtml(s){
  return String(s).replace(/[&<>\"']/g, function(m){return ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":"&#39;"})[m];});
}

function showTyping(on){
  typingEl.style.display = on ? 'block' : 'none';
}

document.getElementById('send').addEventListener('click', ()=>{
  const inp = document.getElementById('msg');
  const text = inp.value.trim();
  if(!text) return;
  inp.value = '';
  sendMessage(text);
});

// allow Enter
document.getElementById('msg').addEventListener('keydown', (e)=>{
  if(e.key === 'Enter'){
    e.preventDefault();
    document.getElementById('send').click();
  }
});

// buttons
document.getElementById('btnJoke').addEventListener('click', ()=>{
  sendMessage('tell me a joke');
});
document.getElementById('btnCalc').addEventListener('click', ()=>{
  const expr = prompt('Enter an expression to calculate (e.g. 2+2 or sqrt(16))');
  if(expr) sendMessage(expr);
});
document.getElementById('btnClear').addEventListener('click', ()=>{
  document.getElementById('chat').innerHTML = '';
});

appendMessage('Bot', "Hi! I can tell jokes and help with problems.", 'bot');
