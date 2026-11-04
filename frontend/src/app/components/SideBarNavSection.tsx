"use client"

import {
  MessageSquare,
  Bookmark
} from "lucide-react";
import { useState } from "react";

function SideBarNavSection() {
  const [activeTab, setActiveTab] = useState("Chats")

  return (
    <div>
        <button 
        onClick={() => setActiveTab("Chats")}
        className={`p-3 flex items-center gap-3 w-full h-13 rounded-2xl font-medium cursor-pointer ${activeTab === 'Chats' ? 'bg-[#0b3247] text-primary' : 'hover:bg-[#0b3247] hover:text-primary transition duration-300 ' }`}
        >
            <MessageSquare size={22} />
            Chats
        </button>
        <button 
        onClick={() => setActiveTab('Saved Trips')}
        className={`p-3 flex items-center gap-3 w-full h-13 rounded-2xl font-medium cursor-pointer ${activeTab === 'Saved Trips' ? 'bg-[#0b3247] text-primary' : 'hover:bg-[#0b3247] hover:text-primary transition duration-300' }`}
        >
            <Bookmark size={22} />
            Saved Trips
        </button>
    </div>
  )
}

export default SideBarNavSection