async function fetchUsers() {
    const res = await fetch('/users');
    const data = await res.json();
    const container = document.getElementById('users');
    container.innerHTML = data.map(u =>
      `<div>
        ${u[0]} - ${u[1]} (${u[2]})
        <button onclick="deleteUser(${u[0]})">Delete</button>
      </div>`
    ).join('');
  }
  
  async function addUser() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    await fetch('/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email })
    });
    fetchUsers();
  }
  
  async function deleteUser(id) {
    await fetch(`/delete/${id}`, { method: 'DELETE' });
    fetchUsers();
  }
  
  window.onload = fetchUsers;

  container.innerHTML = data.map(u =>
    `<div class="user-item">
      <span>${u[1]} (${u[2]})</span>
      <button class="btn btn-sm btn-danger" onclick="deleteUser(${u[0]})">Delete</button>
    </div>`
  ).join('');
  
  