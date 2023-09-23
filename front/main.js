window.onload = () => {
    const usercardsElem = document.getElementById("usercards");
    fetch('http://localhost:8000/users/').then(res => {
        res.json().then(data => {
            console.log(data);

            data.forEach(u => {
               
                const elem = document.createElement("div");
                elem.innerHTML = `
                <div class="usercard">
                    <div class="usercard-name"><div class="label">Name: </div>${u.name}</div>
                    <div class="usercard-info"><div class="label">Username: </div>${u.username}</div>
                    <div class="usercard-info"><div class="label">Mail: </div>${u.mail}</div>
                    <div class="usercard-info"><div class="label">Address: </div>${u.address}</div>
                    <div class="usercard-info"><div class="label">Birthdate: </div>${u.birthdate}</div>
                </div>
                `;
                usercardsElem.appendChild(elem);

            });
        });
    });
};