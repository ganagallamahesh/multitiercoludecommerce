import React, { useEffect } from 'react';
import { CheckCircle2 } from 'lucide-react';

export default function Notification({ message, onClose }) {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, 3500);
    return () => clearTimeout(timer);
  }, [message, onClose]);

  if (!message) return null;

  return (
    <div className="toast-container">
      <div className="toast">
        <CheckCircle2 size={18} color="#38bdf8" />
        <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>{message}</span>
      </div>
    </div>
  );
}
