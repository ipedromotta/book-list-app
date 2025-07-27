import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const useBookStore = defineStore('books', () => {
  const path = 'http://localhost:5000/books'
  const books = ref([])
  const message = ref('')
  const showMessage = ref(false)
  const edit = ref(false)
  const editForm = ref({
    id: '',
    title: '',
    author: '',
    read: false
  })
  const bookForm = ref({
    title: '',
    author: '',
    read: false
  })

  function getBooks() {
    axios.get(path)
      .then((res) => {
        books.value = res.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  function addBook(payload) {
    axios.post(path, payload)
      .then((res) => {
        getBooks();
        showMessageFunc(res.data.message)
      })
      .catch((error) => {
        console.log(error)
        getBooks()
      })
    initForm()
  }

  function updateBook(payload, bookID) {
    const path = `http://localhost:5000/books/${bookID}`
    axios.put(path, payload)
      .then((res) => {
        getBooks()
        showMessageFunc(res.data.message)
      })
      .catch((error) => {
        console.log(error)
        getBooks()
      })
  }

  function deleteBook(closeModal) {
    const path = `http://localhost:5000/books/${editForm.value.id}`
    axios.delete(path)
      .then((res) => {
        getBooks()
        showMessageFunc(res.data.message)
      })
      .catch((error) => {
        console.log(error)
        getBooks()
      })
    closeModal.click()
  }

  function onSubmit(evt, closeModal) {
    evt.preventDefault()

    if (edit.value === true) {
      const payload = {
        title: editForm.value.title,
        author: editForm.value.author,
        read: editForm.value.read
      }
      updateBook(payload, editForm.value.id)
    } else {
      const payload = {
        title: bookForm.value.title,
        author: bookForm.value.author,
        read: bookForm.value.read
      }
      addBook(payload)
    }
    closeModal.click()
  }

  function initForm() {
    bookForm.value.author = ''
    bookForm.value.title = ''
    bookForm.value.read = undefined
  }

  function showMessageFunc(msg) {
    message.value = msg
    showMessage.value = true
    setTimeout(() => {
      showMessage.value = false
    }, 3000)
  }


  return { books, message, showMessage, edit, bookForm, editForm, getBooks, deleteBook, initForm, onSubmit }
})
