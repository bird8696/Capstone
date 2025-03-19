import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState(''); // 백엔드에서 받아올 메시지 저장

  useEffect(() => {
    // 백엔드 API 호출
    fetch('http://localhost:5000')
      .then(response => response.text()) // 백엔드에서 받은 데이터를 텍스트로 변환
      .then(data => setMessage(data)) // 받은 데이터를 상태에 저장
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>🌍 React + Express 연동 성공!</h1>
      <h2>백엔드 메시지입니다: {message}</h2>
    </div>
  );
}

export default App;

