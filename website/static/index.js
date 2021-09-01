
function cancelOrder(orderId) {
  fetch("/cancel-order", {
    method: "POST",
    body: JSON.stringify({ orderId: orderId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
