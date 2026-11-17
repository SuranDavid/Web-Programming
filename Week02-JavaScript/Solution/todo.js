const input = document.getElementById("taskInput");
const list = document.getElementById("tasks");
document.getElementById("addTask").addEventListener("click", addTask);
input.addEventListener("keydown", event => { if (event.key === "Enter") addTask(); });
function addTask() {
    const task = input.value.trim();
    const error = document.getElementById("todoError");
    if (!task) { error.textContent = "Please type a task first."; return; }
    error.textContent = "";
    const li = document.createElement("li");
    const label = document.createElement("label");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.style.display = "inline";
    checkbox.style.width = "auto";
    checkbox.addEventListener("change", () => { li.style.textDecoration = checkbox.checked ? "line-through" : "none"; });
    label.append(checkbox, document.createTextNode(" " + task));
    const remove = document.createElement("button");
    remove.type = "button"; remove.textContent = "Remove";
    remove.addEventListener("click", () => li.remove());
    li.append(label, remove); list.appendChild(li); input.value = ""; input.focus();
}
