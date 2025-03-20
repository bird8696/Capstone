import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./RegisterPage.css"; // CSS 파일 추가
import { motion } from "framer-motion";

const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    phone: "",
    birthdate: "",
    name: "",
  });

  const handleChange = (e) => {
    let { name, value } = e.target;

    // 생년월일 입력을 YYYYMMDD 형식으로 제한
    if (name === "birthdate") {
      value = value.replace(/[^0-9]/g, "").slice(0, 8); // 숫자만 입력 가능 & 8자리 제한
    }

    setFormData({ ...formData, [name]: value });
  };

  const handleRegister = (e) => {
    e.preventDefault();
    console.log("회원가입 데이터:", formData);
    navigate("/login");
  };

  return (
    <div className="register-container">
      <motion.div 
        className="register-box"
        initial={{ opacity: 0, scale: 0.8, y: 50 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
      >
        
        {/* 왼쪽 섹션 */}
        <div className="left-section">
          <h2 className="title">Welcome to Page</h2>
          <p className="subtitle">Sign up to access all features</p>
        </div>

        {/* 오른쪽 섹션 */}
        <div className="right-section">
          <h2 className="title">Sign Up</h2>

          <form onSubmit={handleRegister} className="register-form">
            <label className="input-label">Full Name</label>
            <input
              type="text"
              name="name"
              placeholder="Enter your full name"
              value={formData.name}
              onChange={handleChange}
              className="input-field"
              required
            />

            <label className="input-label">Phone Number</label>
            <input
              type="tel"
              name="phone"
              placeholder="Enter your phone number"
              value={formData.phone}
              onChange={handleChange}
              className="input-field"
              required
            />

            <label className="input-label">Birthdate (YYYYMMDD)</label>
            <input
              type="text"
              name="birthdate"
              placeholder="20000203"
              value={formData.birthdate}
              onChange={handleChange}
              className="input-field"
              required
            />

            {/* 회원가입 버튼 */}
            <button type="submit" className="signup-button">
              Sign Up
            </button>
          </form>

          <p className="login-text">
            Already have an account? {" "}
            <span onClick={() => navigate("/login")} className="login-link">
              Login
            </span>
          </p>
        </div>
      </motion.div>
    </div>
  );
};

export default RegisterPage;
