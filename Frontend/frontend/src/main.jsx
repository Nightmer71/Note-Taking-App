import React from 'react'
import { createRoot } from 'react-dom/client' // Import only createRoot
import { StrictMode } from 'react' // Import StrictMode
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)