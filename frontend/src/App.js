import { Routes, Route } from "react-router-dom";
import About from "./pages/About";
import Form from "./pages/Form";
import Home from "./pages/Home";
import Login from "./pages/Login";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="about" element={<About />} />
      <Route path="form" element={<Form />} />
      <Route path="login" element={<Login />} />
    </Routes>
  );
}

export default App;
