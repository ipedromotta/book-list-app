import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const useBookStore = defineStore('books', () => {
  const path = import.meta.env.VITE_BACKEND
  const books = ref([])
  const message = ref('')
  const showMessage = ref(false)
  const edit = ref(false)
  const editForm = ref({
    ID_BOOK: '',
    TITLE: '',
    AUTHOR: '',
    READ: false
  })
  const bookForm = ref({
    TITLE: '',
    AUTHOR: '',
    READ: false
  })

  function getBooks() {
    var url = `${path}`
    axios.get(url)
      .then((res) => {
        books.value = res.data.payload
      })
      .catch((error) => {
        console.log(error)
      })
  }

  function addBook(payload) {
    var url = `${path}`
    console.log(payload)
    axios.post(url, payload)
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
    var url = `${path}/${bookID}`
    axios.put(url, payload)
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
    var url = `${path}/${editForm.value.ID_BOOK}`
    axios.delete(url)
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
        id: editForm.value.ID_BOOK,
        title: editForm.value.TITLE,
        author: editForm.value.AUTHOR,
        read: editForm.value.READ
      }
      updateBook(payload, editForm.value.ID_BOOK)
    } else {
      const payload = {
        title: bookForm.value.TITLE,
        author: bookForm.value.AUTHOR,
        read: bookForm.value.READ
      }
      addBook(payload)
    }
    closeModal.click()
  }

  function initForm() {
    bookForm.value.AUTHOR = ''
    bookForm.value.TITLE = ''
    bookForm.value.READ = undefined
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
