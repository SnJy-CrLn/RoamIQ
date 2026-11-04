import { PanelLeftClose, Plus} from 'lucide-react'
import Image from 'next/image'

function SideBarHeader() {
  return (
    <div className=''>
       <div className='flex justify-between items-center'>
            <Image
                src="/RoamIQ-sidebar-logo.png"
                alt="RoamIQ AI Travel Agent"
                width={220}
                height={82}
                priority
                className="w-55 h-auto object-contain"
            />        
           <button className="text-secondary-text hover:text-primary transition-colors">
            <PanelLeftClose size={25} strokeWidth={1.8} />
           </button>
       </div> 
        <button className="flex w-full h-13 items-center justify-center gap-3 rounded-2xl bg-primary text-background text-lg font-medium hover:brightness-110 transition">
            <Plus size={22} />
            New Trip
        </button>
    </div>
  )
}

export default SideBarHeader