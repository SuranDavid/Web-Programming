const items = [];
const itemList = document.getElementById("itemList");
const errors = document.getElementById("errors");
const result = document.getElementById("result");

function renderItems() {
    itemList.innerHTML = "";
    if (items.length === 0) {
        itemList.innerHTML = '<li class="empty">No items added yet.</li>';
        return;
    }
    items.forEach((item, index) => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - LKR ${item.cost.toFixed(2)} `;
        const remove = document.createElement("button");
        remove.type = "button";
        remove.textContent = "Remove";
        remove.addEventListener("click", () => { items.splice(index, 1); renderItems(); });
        li.appendChild(remove);
        itemList.appendChild(li);
    });
}

document.getElementById("addItem").addEventListener("click", () => {
    const name = document.getElementById("itemName").value.trim();
    const rawCost = document.getElementById("itemCost").value;
    const cost = Number(rawCost);
    if (!name || rawCost === "" || !Number.isFinite(cost) || cost <= 0) {
        errors.textContent = "Enter an item name and a cost greater than zero.";
        return;
    }
    items.push({ name, cost });
    document.getElementById("itemName").value = "";
    document.getElementById("itemCost").value = "";
    errors.textContent = "";
    renderItems();
});

document.getElementById("calculate").addEventListener("click", () => {
    const peopleRaw = document.getElementById("people").value;
    const people = Number(peopleRaw);
    const tip = Number(document.getElementById("tipRate").value);
    if (items.length === 0) { errors.textContent = "Please add at least one menu item."; return; }
    if (peopleRaw === "" || !Number.isInteger(people) || people < 1) { errors.textContent = "Number of people must be a whole number of at least 1."; return; }
    const subtotal = items.reduce((sum, item) => sum + item.cost, 0);
    const tipAmount = subtotal * tip / 100;
    const total = subtotal + tipAmount;
    errors.textContent = "";
    result.innerHTML = `<strong>Subtotal:</strong> LKR ${subtotal.toFixed(2)}<br><strong>Tip (${tip}%):</strong> LKR ${tipAmount.toFixed(2)}<br><strong>Total:</strong> LKR ${total.toFixed(2)}<br><strong>Each person pays:</strong> LKR ${(total / people).toFixed(2)}`;
});
